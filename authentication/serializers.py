from rest_framework_simplejwt.serializers import TokenObtainPairSerializer # it have model serializers

class custom_token_serializer (TokenObtainPairSerializer): # check 22 video
    def validate(self, attrs):
        data = super().validate(attrs)

        data.update({ # update will merge two dict and create new dict
            'username' : self.user.username # take username key from db (RHS), can add extra fields
        }
        )
        return data