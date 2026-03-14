import json #Сериализация-десериализация json
import os #Работа с файлами
import tomllib #Чтение .toml
import tomli_w #Запись .toml
import zipfile #Чтение архивов
import hashlib #Хеши для сверки файла
import requests #Запросы к Modrinth

from typing import Literal


def makePwToml(download: dict, filename: str, name: str, option: dict = None, side: Literal["both","client","server"] = None, update: dict = None)-> dict:
    toml = {
        "download": download,
        "filename": filename,
        "name": name
    }
    if option: toml["option"] = option
    if side: toml["side"] = side
    if update: toml["update"] = update
    return toml

def scanProjectForVersion(projectId:str, sha1:str = None):
    response = requests.get(f"https://api.modrinth.com/v2/project/{projectId}/version", {
        "loaders": json.dumps(["fabric"]),
        "game_versions": json.dumps(["1.20.1"]),
        "include_changelog": "false"
    })
    if response.status_code == 200:
        for version in response.json():
            for versionFile in version["files"]:
                if not versionFile["primary"]: continue

                if sha1 is None or versionFile["hashes"]["sha1"] == sha1:
                    return version, versionFile

    return None, None


def askModrinth(name:str, sha1:str = None):
    for project in requests.get("https://api.modrinth.com/v2/search", params={
        "query": name,
        "facets": json.dumps([
            ["project_type:mod"], ["categories:fabric"], ["versions:1.20.1"]
        ]),
        "limit": 1,
    }).json()["hits"]:
        version, versionFile = scanProjectForVersion(project["project_id"], sha1)
        if versionFile: return project, version, versionFile
    return None, None, None


if __name__ == "__main__":
    print(os.getcwd())
    os.chdir("pack/mods")
    for path in os.scandir():
        if not path.is_file(): continue

        #Добавление обновлений к .pw.toml
        if path.name.endswith(".pw.toml"):
            file = open(path, "br+")
            pwToml = tomllib.load(file)
            if "update" in pwToml: continue
            print(f"Обработка {pwToml["name"]}", end='')
            option = pwToml.get("option")

            project, version, versionFile = askModrinth(name=pwToml["name"], sha1=pwToml["download"]["hash"])
            if project is None:
                print(" неуспешно")
                continue
            print()

            pwToml["name"] = project["title"]
            pwToml["update"] = {
                "modrinth":{
                    "mod-id":project["project_id"],
                    "version":version["id"]
                }
            }
            file.seek(0)
            tomli_w.dump(pwToml, file)
            file.truncate()

        #Обработка .jar-ников
        elif path.name.endswith(".jar"):
            fabricModJson = json.load(zipfile.ZipFile(path, "r").open("fabric.mod.json", "r"))
            print(f"Обработка {fabricModJson["name"]} ({fabricModJson["id"]})",end='')
            project, version, versionFile = askModrinth(
                name=fabricModJson["id"],
                sha1=hashlib.sha1(open(path, "rb").read()).hexdigest()
            )
            if versionFile:
                tomli_w.dump(
                    makePwToml(
                        download={
                            "hash-format": "sha1",
                            "hash": versionFile["hashes"]["sha1"],
                            "url": versionFile["url"]
                        },
                        filename=versionFile["filename"],
                        name=project["title"],
                        update={
                            "modrinth":{
                                "modrinth": {
                                    "mod-id": project["project_id"],
                                    "version": version["id"]
                                }
                            }
                        }
                    ),
                    open(project["slug"]+".pw.toml", "wb")
                )
                os.remove(path.name)
                print()
            else: print(" неуспешно")

        #Чистка отключённых модов
        elif path.name.endswith(".disabled"): os.remove(path.name)