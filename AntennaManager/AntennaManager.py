import json
import os
import base64
from Crypto.Cipher import AES
from PySide6.QtCore import Slot, Signal, QObject

SECRET_KEY = "jiqwfoef4qognot4"

class FileHandler(QObject):
    fileLoaded = Signal(str, dict)  # Signal emitted when a file is loaded

    def __init__(self, model):
        super().__init__()
        self.model = model

    def encrypt_json(self, data):
        """Encrypt JSON data using AES."""
        json_str = json.dumps(data)
        cipher = AES.new(SECRET_KEY, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(json_str.encode())
        return base64.b64encode(cipher.nonce + tag + ciphertext).decode()

    def decrypt_json(self, encrypted_str):
        """Decrypt AES-encrypted JSON data."""
        try:
            raw_data = base64.b64decode(encrypted_str)
            nonce, tag, ciphertext = raw_data[:16], raw_data[16:32], raw_data[32:]
            cipher = AES.new(SECRET_KEY, AES.MODE_EAX, nonce=nonce)
            return json.loads(cipher.decrypt_and_verify(ciphertext, tag).decode())
        except Exception as e:
            print("Decryption failed:", e)
            return {}

    @Slot(str)
    def loadEncryptedFile(self, fileName):
        """Load and decrypt a selected JSON file."""
        filePath = os.path.join(self.model.directory, fileName)
        if not os.path.exists(filePath):
            print("File not found:", filePath)
            return

        with open(filePath, "r") as file:
            encrypted_data = file.read()

        data = self.decrypt_json(encrypted_data)
        self.fileLoaded.emit(fileName, data)

    @Slot(str, dict)
    def saveEncryptedFile(self, fileName, data):
        """Save JSON data in an encrypted format."""
        filePath = os.path.join(self.model.directory, fileName)
        encrypted_data = self.encrypt_json(data)
        with open(filePath, "w") as file:
            file.write(encrypted_data)

        print(f"Encrypted JSON saved as {fileName}")
        self.model.loadFiles()  # Update ListModel

    @Slot(str)
    def deleteFile(self, fileName):
        """Delete an encrypted file."""
        filePath = os.path.join(self.model.directory, fileName)
        if os.path.exists(filePath):
            os.remove(filePath)
            print(f"Deleted: {fileName}")
            self.model.loadFiles()  # Refresh file list
