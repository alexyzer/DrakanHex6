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


def optimizePack(modsFolder:str):
    dirToReturn = os.getcwd()
    os.chdir(modsFolder)
    modsMetadata = {}
    for path in os.scandir():
        if not path.is_file(): continue

        #Добавление обновлений к .pw.toml
        if path.name.endswith(".pw.toml"):
            pwToml = tomllib.load(open(path, "br+"))
            if "update" not in pwToml or True:
                fileHash = pwToml["download"]["hash"]
                modsMetadata[fileHash] = {"filename": path.name, "local": path.name}
                if "option" in pwToml: modsMetadata[fileHash]["option"] = pwToml["option"]


        #Обработка .jar-ников
        elif path.name.endswith(".jar"):
            #print(f"Хеширование {path.name}", end=' ')
            fileHash = hashlib.sha1(open(path, "rb").read()).hexdigest()
            modsMetadata[fileHash] = {"filename":path.name, "local":path.name}
            #print(fileHash)

        #Чистка отключённых модов
        elif path.name.endswith(".disabled"): os.remove(path.name)


    modrinthVersions = requests.post("https://api.modrinth.com/v2/version_files", json={"hashes":list(modsMetadata), "algorithm": "sha1"}).json()
    for fileHash, version in modrinthVersions.items():
        metadata = modsMetadata[fileHash]
        metadata["project_id"] = version["project_id"]
        metadata["version_id"] = version["id"]
        for file in version["files"]: #Поиск соответствующего файла
            if file["hashes"]["sha1"] == fileHash:
                metadata["filename"] = file["filename"]
                metadata["url"] = file["url"]
                break

    modrinthProjects = requests.get("https://api.modrinth.com/v2/projects",{
        "ids": json.dumps([
            metadata["project_id"] for metadata in modsMetadata.values() if "project_id" in metadata
        ])
    }).json()
    projectsMetadata = {
        project["id"]:{
            "slug":project["slug"],
            "title":project["title"],
            "side":["both","client","server"][len(project["client_side"])==8|(len(project["server_side"])==8)<<1]
        } for project in modrinthProjects
    }
    for metadata in modsMetadata.values():
        if "project_id" in metadata:
            id = metadata["project_id"]
            metadata["slug"] = projectsMetadata[id]["slug"]
            metadata["name"] = projectsMetadata[id]["title"]
            metadata["side"] = projectsMetadata[id]["side"]

    for fileHash, metadata in modsMetadata.items():
        if "url" not in metadata:
            print(f"{metadata["filename"]} нет на Modrinth")
            continue
        pwToml = makePwToml(
            download={
                "hash-format": "sha1",
                "hash": fileHash,
                "url": metadata["url"]
            },
            filename=metadata["filename"],
            name=metadata["name"],
            side=metadata["side"],
            update={
                "modrinth": {
                    "mod-id": metadata["project_id"],
                    "version": metadata["version_id"]
                }
            }
        )
        if "option" in metadata: pwToml["option"] = metadata["option"]
        if "local" in metadata: os.remove(metadata["local"])
        tomli_w.dump(pwToml, open(metadata["slug"]+".pw.toml", "wb"))

    os.chdir(dirToReturn)

if __name__ == "__main__":
    optimizePack("pack/mods")