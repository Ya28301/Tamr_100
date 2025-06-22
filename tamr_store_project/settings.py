from pathlib import Path
import os

# المسار الرئيسي للمشروع
BASE_DIR = Path(__file__).resolve().parent.parent

# مفتاح الأمان (لا تشاركه خارج بيئة التطوير)
SECRET_KEY = 'django-insecure-d@gomkz9zac2$ho_9hzjx!8a78_w8@%f11h_%_dib$)mx@v*jk'

# تفعيل وضع التطوير
DEBUG = True

ALLOWED_HOSTS = []

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

# الوسطاء (Middleware)
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

# قاعدة البيانات
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# تحقق كلمات المرور
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# اللغة والمنطقة الزمنية
LANGUAGE_CODE = 'ar'
TIME_ZONE = 'Asia/Riyadh'

USE_I18N = True
USE_TZ = True

# الملفات الثابتة
STATIC_URL = 'static/'

# إعدادات Cloudinary
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dfteqxxkt',  # ← غيّرها إلى اسم حسابك
    'API_KEY': '737125841525348',        # ← غيّرها إلى مفتاح API الخاص بك
    'API_SECRET': '6R--oPKjKT_0W1LzPzEDR-gh5TU',  # ← غيّرها إلى السر
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# الملفات المرفوعة
MEDIA_URL = '/media/'

# نوع المعرف الافتراضي
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# إعادة التوجيه بعد تسجيل الدخول والخروج
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/accounts/login/'
