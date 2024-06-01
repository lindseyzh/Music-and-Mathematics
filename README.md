# Music-and-Mathematics

北京大学音乐与数学课程大作业(2024春)

代码在music-gen文件夹中，生成的音乐在music文件夹中。报告的Latex源文件在report_src文件夹中。

关于如何查看生成的音乐乐谱, 可以参考 https://web.mit.edu/music21/doc/usersGuide/usersGuide_08_installingMusicXML.html.

### 关于环境配置

[music21官方使用文档](https://web.mit.edu/music21/doc/)

1. 安装music21包 
    ```
    pip install music21
    ```

2. 配置music21
   
    在python环境中输入下列命令:
   
    ```python
    import music21
    music21.configure.run()
    ```
    
    然后一路回车.
   
    music21配置文件会自动检测已安装的MusicXML阅读器. 如果你的电脑上没有可用的MusicXML阅读器, 请参考第3步.
   



4. 安装MusicXML阅读器
   
    (如果你已经安装了MuseScore或者其他MusicXML阅读器, 可以跳过此步.)
   
   [MuseScore](https://musescore.org/en) : music21官方编辑器
    - 从网站上按提示下载并安装MuseHub
    - 通过MuseHub安装MuseScore Studio, 这就是我们需要的MusicXML阅读器
