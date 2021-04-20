from enum import Enum
from typing import List

from .mod_loaders import ModLoaders
from .sites import Sites


class Stabilities(Enum):
    stable = "stable"
    beta = "beta"
    alpha = "alpha"
    unknown = "unknown"


class VersionInfo:
    def __init__(
        self,
        stability: Stabilities,
        mod_loader: ModLoaders,
        site: Sites,
        upload_time: int,
        minecraft_versions: List[str],
        download_url: str,
        filename: str = "",
        name: str = "",
    ) -> None:
        self.stability = stability
        self.mod_loader = mod_loader
        self.repo_type = site
        self.upload_time = upload_time
        self.minecraft_versions = minecraft_versions
        self.download_url = download_url
        self.filename = filename
        self.name = name

    def __str__(self) -> str:
        return f"{self.minecraft_versions}; uploaded {self.upload_time}"

    def __repr__(self) -> str:
        return str(self.__members())

    def __members(self):
        return (
            self.stability,
            self.mod_loader,
            self.repo_type,
            self.upload_time,
            self.minecraft_versions,
            self.download_url,
            self.filename,
            self.name,
        )

    def __eq__(self, other) -> bool:
        if type(other) is type(self):
            return self.__members() == other.__members()
        return False

    def __hash__(self):
        return hash(self.__members())
