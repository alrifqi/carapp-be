from core.database import database

assets_collection = database.get_collection("assets")


async def save_file(filename: str, file_path: str):
    new_brand = await assets_collection.insert_one(
        {"filepath": file_path, "filename": filename, })
    created_assets = await assets_collection.find_one({"_id": new_brand.inserted_id})
    return created_assets
