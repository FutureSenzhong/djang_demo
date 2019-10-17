import os

import celery as celery
import pymysql
from celery.schedules import crontab

from my_blog import settings

pymysql.install_as_MySQLdb()


# 注册环境变量（注册Django配置文件）
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'teamproject.settings')
# 创建Celery的实例并指定broker（消息队列服务）
app = celery.Celery('teamproject', broker='redis://:123456@120.78.155.198:6379/1')
# 读取Django项目的配置信息（例如定时任务需要读取时区）
app.config_from_object('django.conf:settings')
# 从配置文件注册的应用中发现异步任务和定时任务
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# 配置定时任务
app.conf.update(
    timezone=settings.TIME_ZONE,
    enable_utc=True,
    # 定时任务（计划任务）相当于是消息的生产者
    # 如果只有生产者没有消费者那么消息就会在消息队列中积压
    # 将来实际部署项目的时候生产者、消费者、消息队列可能都是不同节点
    beat_schedule={
        'export_emp_excel_task': {
            'task': 'common.tasks.auto_export_excel',
            'schedule': crontab(),
        },
    },
)
