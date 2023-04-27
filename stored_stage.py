from typing import List

class TerrainTypes():
    name: str = ""

class StoredStage():
    name: str = ""
    width: int = 80
    height: int = 80
    terrain: List[List[TerrainTypes]] = []
