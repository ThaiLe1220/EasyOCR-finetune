import os
import git
import shutil
import logging

# Configure logging
logging.basicConfig(
    filename="downloader.log",
    filemode="w",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def download_and_replace_output(repo_url, branch, output_dir):
    """Downloads the 'output/en' directory from a Git repository and replaces the local 'output' directory."""

    repo_dir = "temp_repo"  # Temporary directory for the full clone

    logging.info(f"Cloning repository: {repo_url}")

    try:
        # Full clone of the repository
        git.Repo.clone_from(repo_url, repo_dir, branch=branch)

        # Delete all files except the "output3/en" directory
        for item in os.listdir(repo_dir):
            if item not in (
                "output3",
                ".git",
            ):  # Keep the 'output' folder and '.git' for tracking
                path = os.path.join(repo_dir, item)
                if os.path.isdir(path):
                    shutil.rmtree(path)
                else:
                    os.remove(path)

        # Replace the local 'output' directory
        if os.path.exists(output_dir):
            shutil.rmtree(output_dir)
        shutil.copytree(os.path.join(repo_dir, "output3/en"), output_dir)

        logging.info(f"Output directory updated from the repository")

    except Exception as e:
        logging.error(f"Error updating output directory: {e}")
    finally:
        # Clean up the temporary repository
        if os.path.exists(repo_dir):
            shutil.rmtree(repo_dir)


if __name__ == "__main__":
    repo_url = "https://github.com/ThaiLe1220/TextRecognitionDataGenerator.git"
    branch = "master"
    output_dir = "output/en"

    download_and_replace_output(repo_url, branch, output_dir)
