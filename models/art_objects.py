from typing import List, Optional, Dict, Any
from pydantic import BaseModel


class Department(BaseModel):
    departmentId: int
    displayName: str


class Artist(BaseModel):
    constituentID: Optional[int] = None
    role: Optional[str] = None
    name: Optional[str] = None
    constituentULAN_URL: Optional[str] = None
    constituentWikidata_URL: Optional[str] = None
    gender: Optional[str] = None


class ArtObject(BaseModel):
    objectID: int
    isHighlight: Optional[bool] = None
    accessionNumber: Optional[str] = None
    accessionYear: Optional[str] = None
    isPublicDomain: Optional[bool] = None
    primaryImage: Optional[str] = None
    primaryImageSmall: Optional[str] = None
    additionalImages: Optional[List[str]] = None
    constituents: Optional[List[Artist]] = None
    department: Optional[str] = None
    objectName: Optional[str] = None
    title: Optional[str] = None
    culture: Optional[str] = None
    period: Optional[str] = None
    dynasty: Optional[str] = None
    reign: Optional[str] = None
    portfolio: Optional[str] = None
    artistRole: Optional[str] = None
    artistPrefix: Optional[str] = None
    artistDisplayName: Optional[str] = None
    artistDisplayBio: Optional[str] = None
    artistSuffix: Optional[str] = None
    artistAlphaSort: Optional[str] = None
    artistNationality: Optional[str] = None
    artistBeginDate: Optional[str] = None
    artistEndDate: Optional[str] = None
    artistGender: Optional[str] = None
    artistWikidata_URL: Optional[str] = None
    artistULAN_URL: Optional[str] = None
    objectDate: Optional[str] = None
    objectBeginDate: Optional[int] = None
    objectEndDate: Optional[int] = None
    medium: Optional[str] = None
    dimensions: Optional[str] = None
    measurements: Optional[List[Dict[str, Any]]] = None
    creditLine: Optional[str] = None
    geographyType: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    county: Optional[str] = None
    country: Optional[str] = None
    region: Optional[str] = None
    subregion: Optional[str] = None
    locale: Optional[str] = None
    locus: Optional[str] = None
    excavation: Optional[str] = None
    river: Optional[str] = None
    classification: Optional[str] = None
    rightsAndReproduction: Optional[str] = None
    linkResource: Optional[str] = None
    metadataDate: Optional[str] = None
    repository: Optional[str] = None
    objectURL: Optional[str] = None
    tags: Optional[List[Dict[str, Any]]] = None
    objectWikidata_URL: Optional[str] = None
    isTimelineWork: Optional[bool] = None
    GalleryNumber: Optional[str] = None


class SearchResponse(BaseModel):
    total: int
    objectIDs: Optional[List[int]] = None


class DepartmentsResponse(BaseModel):
    departments: List[Department]