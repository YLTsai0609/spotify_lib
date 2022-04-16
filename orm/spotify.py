import attr
from typing import Dict, List


@attr.s(slots=True, auto_attribs=True, kw_only=True)
class Image:
    pass


@attr.s(slots=True, auto_attribs=True, kw_only=True)
class artist:
    external_urls: Dict[str, str] = None
    href: str = None
    id: str = None
    name: str = None
    type: str = None
    uri: str = None


@attr.s(slots=True, auto_attribs=True, kw_only=True)
class album:
    album_type: str = None
    artists = List[artist] = None
    available_markets = List[str] = None
    external_urls: Dict[str, str] = None
    href: str = None
    id: str = None
    # images : List[Image]
    name: str = None
    release_date: str = None
    release_date_precision: str = None
    total_tracks: int = None
    type: str = None
    uri: str = None


@attr.s(slots=True, auto_attribs=True, kw_only=True)
class Track:
    album: album = None
    artists: List[artist] = None
    available_markets = List[str] = None
    disc_number: int = None
    duration_ms: int = None
    explicit: bool = None
    external_ids: Dict[str, str]
    external_urls: Dict[str, str]
    href: str = None
    id: str = None
    is_local: bool = None
    name: str = None
    popularity: int = None
    preview_url: str = None
    track_number: int = None
    type: str = None
    uri: str = None
