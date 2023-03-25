from api.BoardApi import BoardApi

id_organiz = "62979d9dd164941dd1158909"

def test_creat_board(api_client: BoardApi, delete_board: str):
    name = "Новая доска"
    board_list_before = api_client.get_all_boards_by_org_id(id_organiz)
    create_board = api_client.create_board(name)
    delete_board["board_id"] = create_board.get("id")
    board_list_after = api_client.get_all_boards_by_org_id(id_organiz)

    assert len(board_list_after) - len(board_list_before) == 1
   

def test_delete_board(api_client: BoardApi, create_dummy_board: str):
    board_list_before = api_client.get_all_boards_by_org_id(id_organiz)
    api_client.remove_board(create_dummy_board)
    board_list_after = api_client.get_all_boards_by_org_id(id_organiz)

    assert len(board_list_before) - len(board_list_after) == 1



