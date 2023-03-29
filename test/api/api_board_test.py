from api.BoardApi import BoardApi
import pytest



@pytest.mark.skip
def test_creat_board(api_client: BoardApi, delete_board: str, test_data: dict):
    org_id = test_data.get("id_org")
    name = "Новая доска"
    board_list_before = api_client.get_all_boards_by_org_id(org_id)
    create_board = api_client.create_board(name)
    delete_board["board_id"] = create_board.get("id")
    board_list_after = api_client.get_all_boards_by_org_id(org_id)

    assert len(board_list_after) - len(board_list_before) == 1
   
@pytest.mark.skip
def test_delete_board(api_client: BoardApi, create_dummy_board: str, test_data: dict):
    org_id = test_data.get("id_org")
    board_list_before = api_client.get_all_boards_by_org_id(org_id)
    api_client.remove_board(create_dummy_board)
    board_list_after = api_client.get_all_boards_by_org_id(org_id)


    assert len(board_list_before) - len(board_list_after) == 1



