import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import "../Delegate"

ColumnLayout {
    spacing: 10
    anchors.fill: parent

    Label {
        text: "Tests"
        font.pixelSize: 20
        color: theme.textColor
        font.bold: true
        Layout.alignment: Qt.AlignHLeft
        Layout.leftMargin: 12
        // anchors.left: parent.left
        // anchors.leftMargin: 12
    }

    ListView {
        id: listView
        Layout.fillWidth: true
        Layout.fillHeight: true
        clip: true

        model: ListModel {
            ListElement { name: "Single Port"; value: "Tests the signle port of the antenna" }
            ListElement { name: "Double Port"; value: "Tests the double port of the antenna" }
            ListElement { name: "Multitrace"; value: "Tests the multiple port of the antenna with traces to compare" }
            ListElement {
                name: "Interband"; value: "Tests between two ports"
            }
        }
        delegate: TestsDelegate {}
    }
}
