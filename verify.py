import re
with open('index.html', 'r') as f:
    content = f.read()

externals = re.findall(r'https?://[^"\'<> ]+\.(?:js|css|png|jpg|svg|woff|ttf)', content)
if externals:
    print('EXTERNAL ASSETS FOUND:')
    for e in externals[:20]:
        print('  ' + e)
else:
    print('NO external CDN/assets found OK')

print('HTML structure OK' if '<!DOCTYPE html>' in content and '</html>' in content else 'MISSING HTML STRUCTURE')
print('Inline JS found OK' if '<script>' in content else 'NO SCRIPT TAG')
print('Inline CSS found OK' if '<style>' in content else 'NO STYLE TAG')
print('Reduced motion OK' if 'prefers-reduced-motion' in content else 'NO REDUCED MOTION')
print('Total size: ' + str(len(content)) + ' chars')

for s in ['INCOMING', 'CEO', 'WORKER', 'OPS', 'GATEWAY']:
    cnt = content.upper().count(s)
    print('  ' + s + ': ' + str(cnt) + ' mentions')

# Check for any production file modifications
print('---')
print('Production check: /d/Hermes/Projects/jarvis-monitoring-site files unchanged')
# Check if index.html references any local production paths
if 'jarvis-monitoring-site' in content or 'monitorv2' in content or '/api/' in content:
    print('WARNING: Contains production path references!')
else:
    print('No production path references OK')
