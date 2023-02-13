import boto3
from django.conf import settings


class Bucket:
    """
    CDN Bucket manager
    init method creates connection
    """
    def __int__(self):
        session = boto3.session.Session()
        self.co = session.client(
            service_name=settings.AWS_STORAGE_BUCKET_NAME,
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            endpoint_url=settings.AWS_S3_ENDPOINT_URL,
        )

    def get_objects(self):
        result = self.co.list_objects_v2(Bucket=settings.AWS_STORAGE_BUCKET_NAME)
        if result['KeyCount']:
            return result['Contents']
        else:
            return None

    def delete_object(self, key):
        self.co.delete_object(Bucket=settings.AWS_STORAGE_BUCKET_NAME, Key=key)
        return True


bucket = Bucket()
