from evaluator import evaluate, digit_list, operand_list


class Operations:
    def __init__(self, display_text_widget, expression_label):
        self.display_widget = display_text_widget
        self.expression_label_widget = expression_label
        self.operand_counter = 0

    def update_display(self, value: str):
        self.display_condition()
        self.set_display_text(value)

    def clear_display(self):
        self.display_widget.setText('0')
        self.expression_label_widget.setText('')
        self.operand_counter = 0

    def delete_single_value(self):  # Backspace functionality
        self.display_widget.setText(self.display_widget.text()[0: -1])
        if self.display_widget.text() == '':
            self.display_widget.setText('0')

    def display_condition(self):
        if self.display_widget.text() == '0':
            self.display_widget.setText('')

    def operand_setter(self, value):
        if len(self.display_widget.text()) > 2:
            if value in operand_list and self.display_widget.text()[-2] in operand_list:
                self.display_widget.setText(f"{self.display_widget.text()[0: -2] + value + ' '}")  # replace the operand
                return

        self.display_widget.setText(self.display_widget.text() + ' ' + value + ' ')
        self.multiple_operand_detector()

    def set_display_text(self, value):
        if value in digit_list:
            if self.expression_label_widget.text() != '' and self.operand_counter == 0:
                self.clear_display()
                self.display_widget.setText(value)
                return
            self.display_widget.setText(self.display_widget.text() + value)

        elif value in operand_list:
            self.operand_counter += 1
            self.operand_setter(value)

    def multiple_operand_detector(self):
        if self.operand_counter > 1:
            self.set_calculated_values(self.display_widget.text()[-2])

    def set_calculated_values(self, operand=None):
        if operand is not None:
            result = evaluate(self.display_widget.text()[0: -2])
            self.expression_label_widget.setText(self.display_widget.text()[0: -3] + ' ' + ' ' + '=')
            self.display_widget.setText(str(result) + ' ' + operand + ' ')
            self.operand_counter = 1
        else:
            result = evaluate(self.display_widget.text())
            self.expression_label_widget.setText(self.display_widget.text() + ' ' + ' ' + '=')
            self.display_widget.setText(str(result))
            self.operand_counter = 0
