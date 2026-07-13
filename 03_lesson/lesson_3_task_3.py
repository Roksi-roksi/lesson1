from address import Address
from mailing import Mailing

to_address_1 = Address('344512', 'Ekaterinburg', 'Savkova', '32', '54')
from_address_1 = Address('366011', 'Rostov', 'Tekucheva', '1|14', '39')

mail_1 = Mailing( 2000, 'one')
mail_1.add_address(to_address_1, from_address_1)



print(f"Отправление {mail_1.track} из {mail_1.get_address_to().send()} в {mail_1.get_address_from().send()}. Стоимость {mail_1.cost} рублей.")