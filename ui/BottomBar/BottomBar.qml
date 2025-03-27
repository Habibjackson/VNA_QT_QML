import QtQuick
import QtQuick.Controls.Material
import QtQuick.Layouts
import "../Components"

Rectangle {
    property string text: "Ready"
    property alias indeterminate: progress.indeterminate
    property alias value: progress.value

    id: statusBar
    width: parent.width
    height: 80
    color: theme.backgroundColor
    anchors.bottom: parent.bottom
    anchors.left: parent.left
    anchors.right: parent.right

    ColumnLayout {
        anchors.fill: parent
        anchors.margins: 8

        spacing: 0
        Text {
            id: slidingText
            text: test.progress.status
            font.pixelSize: 24
            color: theme.textColor
            // Layout.alignment: Qt.AlignLeft | Qt.AlignVCenter
        }

        ProgressBar {
            visible: !value == 0
            from: 0
            to: 100
            id: progress
            Layout.fillWidth: true
        }

        // Button {
        //     text: "Click"
        //     onClicked: {
        //         slidingText.y = slidingText.parent.height
        //         slideAnimation.restart()
        //     }
        // }
    }
}
