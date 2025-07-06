import os
from typing import Dict, Any

class Config:
    
    def __init__(self):
        self.config = self._load_config()
        
    def _load_config(self) -> Dict[str, Any]:
        return {
            'API_BASE_URL': os.getenv('API_BASE_URL', 'http://localhost:8000/api'),
            'AUTH_URL': os.getenv('AUTH_URL', 'http://localhost:8000/auth'),
            
            'TEST_USER': os.getenv('TEST_USER', 'sales_user'),
            'TEST_PASSWORD': os.getenv('TEST_PASSWORD', 'password123'),
            
            'DEFAULT_TIMEOUT': int(os.getenv('DEFAULT_TIMEOUT', '30')),
            'PERFORMANCE_TIMEOUT': int(os.getenv('PERFORMANCE_TIMEOUT', '300')),
            
            'DEBUG': os.getenv('DEBUG', 'False').lower() == 'true',
            'LOG_LEVEL': os.getenv('LOG_LEVEL', 'INFO')
        }
        
    def get(self, key: str, default: Any = None) -> Any:
        return self.config.get(key, default)
        
    def set(self, key: str, value: Any):
        self.config[key] = value
        
config = Config()