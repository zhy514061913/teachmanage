from rest_framework import serializers

from user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  # 要序列的model
        fields = ('id', 'name', 'email', 'password')

    # 设置错误提示信息
    name = serializers.CharField(error_messages={
        'name': '用户名不能为空',
        'name': '用户名太长了'
    }, max_length=10)
    email = serializers.CharField(error_messages={
        'email': '电话不能为空',
    }, max_length=11, min_length=11)
