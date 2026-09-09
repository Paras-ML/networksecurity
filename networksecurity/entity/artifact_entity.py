from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    """
    Represents an artifact related to data ingestion in network security.

    Attributes:
        name (str): The name of the artifact.
        type (str): The type of the artifact (e.g., 'log', 'packet', 'alert').
        source (str): The source from which the artifact was ingested.
        timestamp (str): The timestamp when the artifact was created or ingested.
        metadata (dict): Additional metadata associated with the artifact.
    """
    trained_file_path: str
    test_file_path: str 