"""
Build script for TestSnapper desktop app
Creates standalone executables for Windows and macOS
"""
import subprocess
import sys
import os
import platform

APP_NAME = "TestSnapper"
ICON_WIN = "assets/icon.ico"
ICON_MAC = "assets/icon.icns"

def build():
    system = platform.system()
    
    cmd = [
        sys.executable, '-m', 'PyInstaller',
        '--name', APP_NAME,
        '--onefile',
        '--windowed',
        '--add-data', f'../assets{os.pathsep}assets',
        '--clean',
    ]
    
    if system == 'Windows':
        cmd.extend(['--icon', ICON_WIN])
    elif system == 'Darwin':
        cmd.extend(['--icon', ICON_MAC])
        cmd.extend(['--osx-bundle-identifier', 'com.testsnapper.app'])
    
    cmd.append('testsnapper.py')
    
    print(f"Building {APP_NAME} for {system}...")
    subprocess.run(cmd, check=True)
    print(f"✅ Build complete! Check dist/{APP_NAME}")

if __name__ == '__main__':
    import os
    build()
