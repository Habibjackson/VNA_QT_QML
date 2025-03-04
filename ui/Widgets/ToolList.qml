import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import "../Delegate"

ColumnLayout {
    spacing: 8

    Label {
        text: "Tool List"
        font.pixelSize: 20
        color: theme.textColor
        font.bold: true
        Layout.alignment: Qt.AlignHLeft
        Layout.leftMargin: 12
    }

    ListView {
        id: listView
        Layout.fillWidth: true
        Layout.fillHeight: true
        model: ListModel {
            ListElement { name: "Tilt Control"; value: "Get or Set tilt control of the antenna phase shifter" }
            ListElement { name: ""; value: 9.8 }
            ListElement { name: "Device C"; value: 15.2 }
        }
        clip: true
        delegate: ToolListDelegate {}
    }
}
