from fpdf import FPDF
import order
from number_in_words import number_to_words

def rec_num_parser(num):
	if num < 1000:
		return str(int(num))
	return rec_num_parser(num // 1000) + ' ' + str(int(num))[-3:]

def num_parser(num):
	return rec_num_parser(int(num // 1)) + ','\
		 + '%02i' %  int(num * 100 % 100)

def set_unicode_font():
	pdf = FPDF()
	pdf.add_font(
		'DejaVu', '',
		'/usr/share/fonts/truetype/ttf-dejavu/DejaVuSansCondensed.ttf',
		uni=True
	)
	pdf.add_font(
		'DejaVu_bold', '',
		'/usr/share/fonts/truetype/ttf-dejavu/DejaVuSansCondensed-Bold.ttf',
		uni=True
	)
	pdf.set_font('DejaVu', size=8)
	return pdf

def put_multi_cell(pdf, x, y, width, text, algn='L'):
	pdf.x = x
	pdf.y = y
	pdf.multi_cell(width, 4, txt=text, align=algn)

def entity_info(entity):
	info = ', '.join((
		entity.name,
		'ИНН ' + str(entity.inn),
		'КПП ' + str(entity.kpp),
		entity.address
	))
	return info

def delete_bad_fields(pdf):
	pdf.add_page()
	pdf.set_fill_color(255)
	pdf.rect(10, 137, 40, 8, style='F')
	pdf.rect(43, 135, 4, 8, style='F')
	pdf.rect(60, 50, 40, 8, style='F')

def fill_top_rect(pdf):
	put_multi_cell(pdf, 11, 14, 80, order.supplier.bank)
	pdf.text(20, 30.5, txt=str(order.supplier.inn))
	pdf.text(70, 30.5, txt=str(order.supplier.kpp))
	pdf.text(124, 17.5, txt=str(order.supplier.bik))
	pdf.text(124, 21.5, txt=str(order.supplier.bank_accaunt_num))
	pdf.text(124, 30, txt=str(order.supplier.accaunt_num))
	pdf.text(12, 35, txt=order.supplier.name)

def fill_second_rect(pdf):
	put_multi_cell(pdf, 20, 100, 80, order.mobile_product)
	put_multi_cell(pdf, 20, 104, 80, order.traffic_product)
	put_multi_cell(pdf, 133, 100, 23, num_parser(order.mobile_price), 'R')
	put_multi_cell(pdf, 133, 104, 23, num_parser(order.traffic_price), 'R')
	put_multi_cell(pdf, 155, 100, 27, num_parser(order.amount), 'R')


def main():
	pdf = set_unicode_font()
	delete_bad_fields(pdf)
	fill_top_rect(pdf)
	fill_second_rect(pdf)
	pdf.set_font('DejaVu_bold', size=8)
	put_multi_cell(pdf, 155, 119, 27, num_parser(order.amount), 'R')
	put_multi_cell(pdf, 155, 123.5, 27, num_parser(order.amount / 6), 'R')
	put_multi_cell(pdf, 155, 128, 27, num_parser(order.amount), 'R')
	pdf.text(
		45, 136.3,
		txt='2, на сумму ' + num_parser(order.amount) + ' руб.'
	)
	pdf.text(
		12, 141,
		txt = number_to_words(order.amount)
	)
	pdf.set_font('DejaVu_bold', size=12)
	pdf.text(57, 54, txt=str(order.bill_num) + ' от ' + order.bill_date)
	pdf.set_font('DejaVu_bold', size=8)
	put_multi_cell(pdf, 35, 63, 145, entity_info(order.supplier))
	put_multi_cell(pdf, 35, 75, 145, entity_info(order.customer))
	put_multi_cell(pdf, 35, 87.5, 145,
					'№' + str(order.num) + ' от ' + order.date)
	pdf.set_font('DejaVu', size=8)
	put_multi_cell(pdf, 40, 175, 67, order.leader, 'R')
	put_multi_cell(pdf, 135, 175, 48, order.accountant, 'R')
	pdf.output('info.pdf')

if __name__ == "__main__":
	main()

	
