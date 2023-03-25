import requests


class BoardApi:

    def __init__(self, base_url: str, token: str):
        self.base_url = base_url
        self.token = token
    
    def get_all_boards_by_org_id(self, org_id: str) -> dict:
        path = "{trello}organization/{id}?boards=open&board_fields=all&fields=boards".format(trello = self.base_url ,id = org_id)
        cookie = {"token" : self.token}
        resp = requests.get(path, cookies=cookie)

        return resp.json().get("boards")
    
    def create_board(self, name: str, default_lists: bool = True) -> dict:
        body = {
            "defaultLists" : default_lists,
            "name" : name,
            "token" : self.token
        }
        cookie = {"token" : self.token}

        path = "{trello}/boards/".format(trello = self.base_url)
        resp = requests.post(path, json=body, cookies=cookie)
        return resp.json()
    
    def remove_board(self, id_board: str):
        cookie = {"token" : self.token}
        
        path = "{trello}boards/{id}".format(trello = self.base_url, id = id_board)
        requests.delete(path, cookies=cookie)
