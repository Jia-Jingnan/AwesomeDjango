import os


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "echo.settings")
    import django
    django.setup()
    # 测试代码
    from app01 import models
    models.User.objects.all()
