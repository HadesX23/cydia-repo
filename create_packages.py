import os
import apt_pkg

def main():
    apt_pkg.init()
    deb_files = [f for f in os.listdir('./debs') if f.endswith('.deb')]
    package_infos = []

    for deb_file in deb_files:
        deb = apt_pkg.TagFile(open(f'./debs/{deb_file}', 'rb'))
        package_info = deb.section
        package_info['Filename'] = f'debs/{deb_file}'
        package_info['Size'] = os.path.getsize(f'./debs/{deb_file}')
        package_infos.append(package_info)

    with open('Packages', 'w') as f:
        for package_info in package_infos:
            for key, value in package_info.items():
                f.write(f'{key}: {value}\n')
            f.write('\n')

if __name__ == '__main__':
    main()
