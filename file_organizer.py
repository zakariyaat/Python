import os
import shutil

# Define file categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Others": []
}

def organize_files(folder_path):
    if not os.path.exists(folder_path):
        print("❌ The specified folder does not exist.")
        return
    
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(filename)[1].lower()
            moved = False
            
            for category, extensions in FILE_TYPES.items():
                if file_ext in extensions:
                    category_folder = os.path.join(folder_path, category)
                    os.makedirs(category_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(category_folder, filename))
                    print(f"Moved {filename} → {category}/")
                    moved = True
                    break
            
            if not moved:  # If no category matched
                other_folder = os.path.join(folder_path, "Others")
                os.makedirs(other_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(other_folder, filename))
                print(f"Moved {filename} → Others/")

def main():
    folder_path = input("Enter the folder path to organize: ")
    organize_files(folder_path)
    print("\n✅ Files organized successfully!")

if __name__ == "__main__":
    main()
