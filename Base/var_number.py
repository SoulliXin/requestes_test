class Globle_var:
    case_id = 0
    is_run = 2
    condition_nb = 3
    depend_key_nb = 4
    url_nb = 5
    method_nb = 6
    data_nb = 7
    cookie_nb = 8
    header_nb = 9
    expected_way_nb = 10
    expected_result = 11
    result_nb = 12
    response_nb = 13

    def get_case_id(self):
        return Globle_var.case_id

    def get_is_run_nb(self):
        return Globle_var.is_run

    def get_condition_nb(self):
        return Globle_var.condition_nb

    def get_depend_way_nb(self):
        return Globle_var.depend_key_nb

    def get_url_nb(self):
        return Globle_var.url_nb

    def get_method_nb(self):
        return Globle_var.method_nb

    def get_data_nb(self):
        return Globle_var.data_nb

    def get_cookie_nb(self):
        return Globle_var.cookie_nb

    def get_header_nb(self):
        return Globle_var.header_nb

    def get_expected_way_nb(self):
        return Globle_var.expected_way_nb

    def get_expected_result(self):
        return Globle_var.expected_result

    def get_result_nb(self):
        return Globle_var.result_nb

    def get_response_nb(self):
        return Globle_var.response_nb


var = Globle_var()