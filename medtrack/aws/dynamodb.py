import boto3

dynamodb = boto3.resource(
    "dynamodb",
    region_name="ap-south-1"
)

users_table = dynamodb.Table("UsersTable")
appointments_table = dynamodb.Table("AppointmentsTable")
diagnoses_table = dynamodb.Table("DiagnosesTable")