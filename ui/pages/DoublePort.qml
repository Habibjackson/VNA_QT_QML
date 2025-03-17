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
            color: "#360d2d"
            title: "Single Port Testing"
        }
        RowLayout {
            Label {
                text: qsTr("Antenna Model")
                color: theme.textColor
            }
            
        }
    }
}
