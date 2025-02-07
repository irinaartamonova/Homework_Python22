from address import Address
from mailing import Mailing

to_address = Address(index="111000", city="Москва", street="Тверская", house="3", apartment="1")
from_address = Address(index="222000", city="Ташкент", street="Независимости", house="11", apartment="30")

mailing = Mailing(to_address=to_address, from_address=from_address, cost=300, track="GGG564895")

output = (
    f"Отправление {mailing.track} из {mailing.from_address.index}, "
    f"{mailing.from_address.city}, {mailing.from_address.street}, {mailing.from_address.house} "
    f"- {mailing.from_address.apartment} в {mailing.to_address.index}, "
    f"{mailing.to_address.city}, {mailing.to_address.street}, {mailing.to_address.house} "
    f"- {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей."
)

print(output)
