import os
import git
import shutil
import logging

# Configure logging (same as before)
logging.basicConfig(
    filename="downloader.log",
    filemode="w",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def download_and_replace_output(repo_url, branch, output_dir):
    """Downloads the 'output/vi' directory from a Git repository and replaces the local 'output' directory."""

    repo_dir = "temp_repo"  # Temporary directory for the partial clone

    logging.info(f"Cloning repository: {repo_url} (output/vi folder only)")

    try:
        # Sparse checkout: Download only the 'output/vi' directory
        git.Repo.clone_from(
            repo_url,
            repo_dir,
            branch=branch,
            no_checkout=True,  # Avoid checking out all files
            depth=1,  # Limit to one directory level
            sparse_paths=["output/vi"],
        )

        # Clear and replace the local 'output' directory
        if os.path.exists(output_dir):
            shutil.rmtree(output_dir)
        shutil.copytree(os.path.join(repo_dir, "output/vi"), output_dir)

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
    output_dir = "output"

    download_and_replace_output(repo_url, branch, output_dir)
