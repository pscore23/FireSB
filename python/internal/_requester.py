from urllib import request, error


class Require:
    @staticmethod
    def get_project_data(p_id):
        if len(p_id) == 0:
            return None

        else:
            url = f"https://projects.scratch.mit.edu/{p_id}/"

        try:
            return request.urlopen(url).read().decode("utf-8")

        except (error.HTTPError, UnicodeEncodeError):
            return None
