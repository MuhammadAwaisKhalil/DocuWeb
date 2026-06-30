from pydantic import BaseModel, Field
from typing import List

#C++ styled arrays --> List
#Inherits from basemodel as it becomes a structured data representation..data returned from llm is converted to this format
#LLM can read descriptions of attributes to further gain context about type of info it returns
class Node(BaseModel):
    id: str = Field(
        description="Unique, capitalized name of the entity."
    )

    type: str = Field(
        description="The category of the entity. (eg.. Person, Organization, Book...)"
    )

    significance: str = Field(
        description="A 1-2 sentence explanation of why this entity is important in this context or what is its purpose"
    )

class Edge(BaseModel):
    source: str = Field(
        description="The exact id of the starting node."
    )

    target: str = Field(
        description="The exact id of the destination node"
    )

    relationship: str = Field(
        description="A short snake_cased verb describing the relationship between source and target. (e.g founded_by, plays, lost_to....)"
    )

#Above classes are an internal skeleton of how the graph is structired and how relationships between nodes shall be maintained
#Graph class defines components if the graph and ties them together

class KnowledgeGraph(BaseModel):
    nodes: List[Node] = Field(
        default=[],
        description="A complete list of all unique entities extracted from the text."
    )
    edges: List[Node] = Field(
        default=[],
        description="A complete list of all directed relationships between the nodes"
    )