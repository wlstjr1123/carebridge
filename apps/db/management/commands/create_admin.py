from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from django.utils import timezone
from apps.db.models.users import Users

class Command(BaseCommand):
    help = '비밀번호 1234를 가진 ADMIN 사용자를 생성합니다.'

    def handle(self, *args, **options):
        username = 'admin_user'
        
        # 중복 생성 방지
        if Users.objects.filter(username=username).exists():
            self.stdout.write(self.style.WARNING(f"'{username}'이(가) 이미 존재합니다."))
            return

        try:
            user = Users.objects.create(
                username=username,
                password=make_password('1234'), # Django 설정에 맞는 해시 자동 생성
                name='관리자',
                gender='M',
                phone='010-1234-5678',
                email='admin@example.com',
                resident_reg_no='900101-1234567',
                mail_confirm='Y',
                address='서울특별시 강남구 테헤란로 123',
                provider='local',
                provider_id=None,
                provider_email=None,
                role='ADMIN',
                withdrawal='0',
                created_at=timezone.now()
            )
            self.stdout.write(self.style.SUCCESS(f"성공적으로 관리자({username}) 계정을 생성했습니다!"))
            
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"에러 발생: {e}"))