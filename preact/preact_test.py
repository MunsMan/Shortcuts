import os
from preact import Manager
import shutil

MANAGER = Manager()


def test_module() -> None:
    MANAGER.setName("moduleTest")
    MANAGER.createModule()
    compareFiles("index.tsx", "moduleTest")
    compareFiles("style.css", "moduleTest")
    compareFiles("style.css.d.ts", "moduleTest")
    shutil.rmtree(os.path.join(
        os.path.abspath(os.getcwd()), "moduleTest"), ignore_errors=True)
    print("[Test Module] - Success - created, compared, deleted")


def test_file() -> None:
    MANAGER.setName("fileTest")
    MANAGER.createFile()
    compareFiles("index.tsx", "fileTest")
    shutil.rmtree(os.path.join(
        os.path.abspath(os.getcwd()), "fileTest"), ignore_errors=True)
    print("[Test File] - Success - created, compared, deleted")


def test_module_with_storybook() -> None:
    MANAGER.setName("moduleTestStory")
    MANAGER.createModule()
    MANAGER.createStorybook()
    compareFiles("index.tsx", "moduleTestStory")
    compareFiles("style.css", "moduleTestStory")
    compareFiles("style.css.d.ts", "moduleTestStory")
    compareFiles("index.stories.tsx", "moduleTestStory")
    shutil.rmtree(os.path.join(
        os.path.abspath(os.getcwd()), "moduleTestStory"), ignore_errors=True)
    print("[Test Module Storybook] - Success - created, compared, deleted")


def compareFiles(filename: str, module: str = "") -> None:
    wdir = os.path.abspath(os.getcwd())
    testFile = open(os.path.join(wdir, "{m}/{n}".format(m=module, n=filename)))
    solutionFile = open(os.path.join(wdir, "presets/{n}". format(n=filename)))
    testText = testFile.read()
    testText = testText.replace(module[0].upper() + module[1:], "Name")
    testText = testText.replace(module, "name")
    assert testText == solutionFile.read()
