# clone git repository to local
import git

git_url = "https://github.com/PhonePe/pulse.git"
dest_path = r"C:\Users\nisha\OneDrive\Desktop\Nisha\GUVI\MiniProject\PhonePeTransInsights\Data"
git.Repo.clone_from(git_url,dest_path)
print("Repository cloned successfully")