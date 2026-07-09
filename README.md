# Tech Services API - Backend Core

نظام Backend متكامل للخدمات التقنية، مصمم لتوفير واجهة برمجية (API) آمنة وسريعة لدعم تطبيقات الموبايل والويب. يركز المشروع على هيكلية البيانات المرنة (Flexible Categorization) ونظام مصادقة (Authentication) عالي المستوى.

## 🛠 التقنيات المستخدمة (Tech Stack)
- **Framework:** Django & Django REST Framework (DRF)[cite: 3, 5, 9]
- **Database:** Django ORM[cite: 5]
- **Security:** SimpleJWT (Token-based Authentication), Password Validation[cite: 7, 9]
- **Architecture:** Clean Architecture approach[cite: 5]

## المميزات الرئيسية
- **نظام مصادقة متكامل:** تسجيل مستخدمين (Signup) ودخول (Login) آمن مع حماية ضد محاولات الوصول غير المصرح بها[cite: 7, 9].
- **إدارة المحتوى:** هيكلية ذكية لتصنيف القوالب (Templates) ودعم الحالات المالية (مجاني/مدفوع)[cite: 2, 5].
- **API Architecture:** واجهات برمجية RESTful توفر استجابات بتنسيق JSON، مما يسهل التكامل مع تطبيقات Flutter[cite: 3, 5].
- **التحقق من البيانات:** استخدام Serializers متقدمة لضمان سلامة البيانات قبل حفظها[cite: 3, 7].

## كيف يعمل المشروع
1. تأكد من وجود Python وتثبيت المتطلبات: 
   `pip install -r requirements.txt`
2. إعداد قاعدة البيانات وعمل Migrations:
   `python manage.py makemigrations`
   `python manage.py migrate`
3. تشغيل السيرفر المحلي:
   `python manage.py runserver`

##  الأمان (Security Measures)
- تطبيق معايير `Django Password Validation` لضمان قوة كلمات المرور[cite: 7].
- استخدام **JWT (JSON Web Tokens)** لإدارة الجلسات بشكل آمن في الأنظمة الموزعة[cite: 9].
- معالجة أخطاء المصادقة بإرجاع `401 Unauthorized` لزيادة مستوى الأمان[cite: 9].

- **Abdallah Mohamed (Migo)** - Backend Developer & Security Architect
