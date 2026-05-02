# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['/Users/antonio/Documents/GitHub/skill-soul-private-ai-suite-mac/src/standalone_app.py'],
    pathex=[],
    binaries=[],
    datas=[('/Users/antonio/Documents/GitHub/skill-soul-private-ai-suite-mac/model-presets', 'model-presets'), ('/Users/antonio/Documents/GitHub/skill-soul-private-ai-suite-mac/runtime-bin-mac', 'runtime-bin-mac'), ('/Users/antonio/Documents/GitHub/skill-soul-private-ai-suite-mac/image-backend-bin-mac', 'image-backend-bin-mac'), ('/Users/antonio/Documents/GitHub/skill-soul-private-ai-suite-mac/ocr-bin-mac', 'ocr-bin-mac')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Offline-AI-Workstation',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch='arm64',
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Offline-AI-Workstation',
)
app = BUNDLE(
    coll,
    name='Offline-AI-Workstation.app',
    icon=None,
    bundle_identifier='com.offlineai.workstation',
)
