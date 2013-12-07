{
  'targets': [
    {
      'target_name': 'openni',
      'sources': [
        'src/Callbacks.cc',
        'src/Context.cc'
      ],
      
      'conditions': [
        ['OS=="mac"', {
            'include_dirs': [
              '/usr/local/include/ni'
            ],
            'link_settings': {
                'libraries': [
                    '/usr/local/lib/libOpenNI.dylib'
                ],
            }
          }, {
            'include_dirs': [
              '/usr/include/ni'
            ],
          }
        ],
        ['OS=="linux"', {
            'link_settings': {
                'libraries': [
                    '/usr/lib/libOpenNI.so'
                ],
            }
          }
        ]
      ]
    }
  ]
}
