import QtQuick
import QtQuick.Controls.Material
import QtQuick.Layouts
import "../Delegate"

ColumnLayout {
    spacing: 10
    anchors.fill: parent

    Label {
        text: qsTr("Manage Antenna")
        font.pixelSize: 20
        color: theme.textColor
        font.bold: true
        Layout.alignment: Qt.AlignLeft
        Layout.leftMargin: 12
    }

    ListView {
        id: listView
        Layout.fillWidth: true
        Layout.fillHeight: true
        clip: true
        currentIndex: 0        
        model: antennaModel
        delegate: TestsDelegate {}
    }
}
