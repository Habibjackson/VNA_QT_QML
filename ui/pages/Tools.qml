import QtQuick
import QtQuick.Controls.Material
import QtQuick.Layouts
import "../Components"
import "../Widgets"

Paper {
    id: testsPage
    ColumnLayout {
        spacing: 10
        height: parent.height
        width: parent.width

        TitleBar {
            Layout.fillWidth: true
            Layout.alignment: Qt.AlignTop
            color: "#640026"
            title: "Tools"
        }
    }
}
