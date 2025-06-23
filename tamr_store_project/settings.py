from pathlib import Path
import os
from decouple import config
import dj_database_url

# المسار الرئيسي للمشروع
BASE_DIR = Path(__file__).resolve().parent.parent

# مفتاح الأمان من متغير البيئة
SECRET_KEY = config('SECRET_KEY')

# وضع التطوير/الإنتاج
DEBUG = config('DEBUG', default=False, cast=bool)

# السماح بجميع المضيفين مؤقتًا (يمكنك تخصيصه لاحقًا)
ALLOWED_HOSTS = ['*']

# التطبيقات المثبتة
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # تطبيقات المشروع
    'accounts',
    'products',
    'orders',

    # Cloudinary
    'cloudinary',
    'cloudinary_storage',
]

# الوسطاء
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ملف الروابط الرئيسي
ROOT_URLCONF = 'tamr_store_project.urls'

# إعدادات القوالب
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# تطبيق WSGI
WSGI_APPLICATION = 'tamr_store_project.wsgi.application'

# إعداد قاعدة البيانات عبر DATABASE_URL
DATABASES = {
    'default': dj_database_url.config(default=config('DATABASE_URL'))
}

# التحقق من كلمات المرور
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# اللغة والمنطقة الزمنية
LANGUAGE_CODE = 'ar'
TIME_ZONE = 'Asia/Riyadh'

USE_I18N = True
USE_TZ = True

# الملفات الثابتة
STATIC_URL = '/static/'

# إعدادات Cloudinary
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': config('CLOUD_NAME'),
    'API_KEY': config('CLOUD_API_KEY'),
    'API_SECRET': config('CLOUD_API_SECRET'),
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# الملفات المرفوعة
MEDIA_URL = '/media/'

# نوع المعرف الافتراضي
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# إعادة التوجيه بعد تسجيل الدخول والخروج
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/accounts/login/'
