@echo off
echo Updating local files with the latest changes...
git pull origin main

echo.
echo Adding updated files to the staging area...
git add .

echo.
echo Committing changes...
git commit -m "Update with MultiBand Diffusion integration"

echo.
echo Pushing changes to GitHub...
git push origin main

echo.
echo Update complete!
pause
