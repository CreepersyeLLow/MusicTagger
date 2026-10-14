# build_macos.spec
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['MusicTager/main.py'],  # 你的主程序文件名，请根据实际情况修改
    pathex=[],
    binaries=[],
    datas=[('image-folder', 'image-folder')],  # 如果程序需要读取图片资源，请包含进来
    hiddenimports=[
        'PyQt6',
        'mutagen',
        'requests',
        # 如果有其他隐式导入，也加在这里
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='MusicTagger',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,  # GUI 程序设置为 False
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch='arm64',  # 明确指定目标架构为 arm64
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='MusicTagger',
)
app = BUNDLE(
    coll,
    name='MusicTagger.app',
    icon=None,  # 如果有图标，可以指定 .icns 文件路径
    bundle_identifier='com.example.musictagger',
)
