from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

'''
    - Only a user can share a 'Share chat'
    - A share must have title
    - A share must have content
    - A share can have an image 
'''
class Share(models.Model) :
    '''
    title_max_length = 100 
    share_contents_max_length = 1000
    '''
    title_max_length = 100
    share_contents_max_length = 1000

    user = models.ForeignKey(User , on_delete=models.CASCADE)

    title = models.TextField(max_length =title_max_length, null=False, blank=False)

    share_content = models.TextField(max_length =share_contents_max_length, null=False, blank=False)

    cover_image = models.ImageField(upload_to= 'photos/', blank=True , null=True )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now= True)

    def __str__(self) :
        return f'{self.user.username} posted "{self.title}"'
