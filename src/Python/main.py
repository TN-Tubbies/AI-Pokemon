from processing.move_processing import get_move_dict

if __name__ == '__main__':
    redo_setup_db = input("Do you want to re-process all databases? (y/n, default no): ")
    if redo_setup_db not in ["", "no"]:
        # Reprocessing all databases
        
        # Get the moves available
        moves = get_move_dict("fr")
        print(moves)