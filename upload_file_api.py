#!/usr/bin/env python

from apiclient import errors
from apiclient.http import MediaFileUpload

import os
import sys
import time
import random
# import settings
import traceback
from httplib2 import Http
from googleapiclient.discovery import build
# import gdata.sites.client
# from gdata import gauth
from oauth2client.client import SignedJwtAssertionCredentials


class Connection:
    http_auth = None
    credential = None

    def __authorize(self, scope=None, sub_email=''):
        private_file_path = "valeo-is-gapis-vtds-prod.p12"

        private_file = file(private_file_path, 'rb')
        private_key = private_file.read()
        private_file.close()

        self.credential = SignedJwtAssertionCredentials(
            "vtds-prod@valeo-is-gapis.iam.gserviceaccount.com",
            private_key,
            scope,
            sub=sub_email)
        self.http_auth = self.credential.authorize(Http())

    def create_directory_service(self, sub_email="meenakshi.sundar@valeo.com"):       #For extract all users in valeo.com
        scope = "https://www.googleapis.com/auth/drive"
        self.__authorize(scope=scope, sub_email=sub_email)
        dirve_service = build('drive', 'v3', http=self.http_auth)
        return dirve_service


def fetch_my_drive_files(username):
            __conn = Connection()
            service = __conn.create_directory_service(username)

            FILES = ['hello.txt','hello.txt']

            for filename in FILES:
                metadata = {'title': filename}
                res = service.files().create(body=metadata,
                        media_body=filename).execute()
                if res:
                    print('Uploaded "%s" (%s)' % (filename, res['mimeType']))



test=fetch_my_drive_files("meenakshi.sundar@valeo.com")
