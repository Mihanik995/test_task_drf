from rest_framework.exceptions import ValidationError


class ProviderValidator:
    def __call__(self, attrs):
        if 'provider' in attrs.keys() and attrs['role'] == 'manufacture' and attrs['provider'] != None:
            raise ValidationError({
                "frequency": "Manufacture cannot have providers"
            })
