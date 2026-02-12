ServerEvents.recipes(event => {
	event.shapeless("hexcasting:battery", [Item.of("hexcasting:battery"), Item.of("hexcasting:battery")]).modifyResult((grid, result) => {
		let phials = grid.findAll(Item.of("hexcasting:battery"))
		let media = 0
		let nbt
		phials.forEach(phial => {
			media += phial.nbt["hexcasting:media"]
			if (phial.nbt != null) nbt = phial.nbt
		});
		if (nbt == undefined) return itemstack
		media = Math.min(Math.max(media,0),2000000000)
		nbt["hexcasting:media"] = Math.trunc(media*Math.sqrt(media/2000000000))
		nbt["hexcasting:start_media"] = Math.trunc(media)
		return result.withNBT(nbt)
	});
});
