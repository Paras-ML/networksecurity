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


@dataclass
class DataValidationArtifact:
    """
    Represents an artifact related to data validation in network security.

    Attributes:
        name (str): The name of the artifact.
        type (str): The type of the artifact (e.g., 'validation_report', 'validation_summary').
        source (str): The source from which the artifact was generated.
        timestamp (str): The timestamp when the artifact was created or validated.
        metadata (dict): Additional metadata associated with the artifact.
    """
    validation_status: bool
    valid_train_file_path: str
    valid_test_file_path: str
    invalid_train_file_path: str
    invalid_test_file_path: str
    drift_report_file_path: str   


@dataclass
class DataTransformationArtifact:
    transformed_object_file_path:str
    transformed_train_file_path:str
    transformed_test_file_path:str